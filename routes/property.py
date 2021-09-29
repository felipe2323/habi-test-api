from exceptions.property import PropertyInfoException, PropertyInfoNotFoundError
from typing import List
from fastapi import APIRouter, HTTPException, Query
from config.db import conn
from sqlalchemy import text
# from models.index import properties, status, status_histories
# If you need to use ORM, please uncomment

# Main Router
property_ = APIRouter()

# Main SQL
global_sql = """
SELECT 
    P.address, 
    P.city, 
    S.name,
    P.price,
    P.description
FROM property P 
LEFT JOIN status_history SH ON SH.id = (
	SELECT id FROM status_history SHH WHERE SHH.property_id = P.id 
	ORDER BY SHH.id DESC 
	LIMIT 1
)
LEFT JOIN status S ON SH.status_id  = S.id
WHERE SH.status_id IS NOT NULL
"""

""" API Routes """

@property_.get('/')
async def get_home():
    """[Get Home ]

    Returns:
        JSON Response with a small introductory message
    """
    return {"msg": "Home Microservice"}


@property_.get('/properties')
async def get_properties(
                year: List[int] = Query([]), 
                status: List[str] = Query([]), 
                cities: List[str] = Query([])):  

    """[Get Properties List With Filters]
    Args:
        year (List: int): list of possible year values.
            ex: [2021, 2020, 2015]
        status (List: str): list of possible status value
            ex: ['','','']
        cities (List: str): list of possible cites value
            ex: ['','','']
    Raises:
        HTTPException
    Return:
        JSON Response with the filtered property list
    Optional:
        To use ORM
        return conn.execute(properties.select()).fetchall()
    """     
    try: 
        sql = global_sql   
        params = dict()
        if year:        
            year_sql = """ AND P.year IN :year"""
            params.update({
                'year': tuple(year)
            })
            sql += year_sql
        if status:        
            status_sql = """ AND S.name IN :status"""
            params.update({
                'status': tuple(status)
            })
            sql += status_sql
        if cities:        
            cities_sql = """ AND P.city IN :cities"""
            params.update({
                'cities': tuple(cities)
            })
            sql += cities_sql  
        properties_info = conn.execute(text(sql), params).fetchall()
        if not properties_info:
            raise PropertyInfoNotFoundError
        return properties_info    
        
    except PropertyInfoException as pie:
        raise HTTPException(**pie.__dict__)
    

@property_.get('/properties/{id}')
async def get_properties_by_id(id: int):
    """[Get Property by id]    
    Args:
        id (int): Property identifier
    Raises:
        HTTPException        
    Return:
        JSON Response with the property
    Optional:
        To use ORM
        return conn.execute(properties.select().where(properties.c.id == id)).fetchall()
    """ 
    try:
        sql = global_sql    
        sql += """ AND P.id = :id"""
        property_info = conn.execute(text(sql), {'id': id}).fetchall()
        if not property_info:
            raise PropertyInfoNotFoundError
        return property_info
    except PropertyInfoException as pie:
        raise HTTPException(**pie.__dict__)