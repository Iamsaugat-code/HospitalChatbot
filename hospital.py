
from datetime import date
import time
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hospital_server")

@mcp.tool()
async def aboutHospital(query:str)->str:
    """provide the information relate hospital, about hospital,details of hospital"""
    return """
    show the result in list.
    1. Name : Abacus Hospital,
    2. Establishment : 2007-07-9 BS,
    3. Location : Mechinagar - 1, jhapa,
    4. Fonder : Lokas Bom,
    5. No of Doctor : 45,
    6. CEO : Arjit Katiwada,
    7. No of Nurse : 150,
    8. Awards : Best Hospital of 2026, Nabinnepal Awards(2001,2002,2003),
    9. Technology : New Advanced technology of 2026

    This tool should be used for any general question related to
    hospitals or hospital details. Return only the information
    provided by the hospital system.
    """

@mcp.tool()
async def founder(query:str)->str:
    """provide the information relate to founder,producer"""
    return " Founder of Abacus Hosiptal is Lokas Bam"

@mcp.tool()
async def CEO(query:str)->str:
    """provide the information relate to CEO"""
    return "CEO of Abacus Hosiptal is Arjit Khatiwada"
@mcp.tool()
async def HeadDocotor(query:str)->str:
    """provide the information relate to HeadDoctor"""
    return "Head Doctor of Abacus Hosiptal is Rupas Neupana"

@mcp.tool()
async def service(query:str)->str:
    """provide information relate to sevice and treatment given by hosiptal"""
    return f"output : {query}"

@mcp.tool()
async def ListofDoctor(query:str)->str:
    """provide the information relate to list of doctor,number of doctor,doctor and their role"""
    return """ show them in table form
        NameDr. Rajesh Sharma 
        Cardiologist
         Dr. Sita Thapa	Pediatrician
         Dr. Amit Joshi	Neurologist
         Dr. Priya Adhikari	Dermatologist
         Dr. Ramesh Karki	Surgeon
         Dr. Nisha Shrestha	Gynecologist
             """

@mcp.tool()
async def contactNumber(query:str)->str:
    """Provide contact information related to doctors, hospital phone numbers, hospital contact numbers, and hospital numbers."""
    return """
    1. Dr. Sita Thapa - 90879
    2. Dr. Amit Joshi - 90800
    3. Dr. Priya Adhikari - 8992
    4. Dr. Ramesh Karki - 4566
    5. Dr. Nisha shrestha - 889
    6. Dr rajesh sharma - 113
    provide the role of doctor by using 'ListofDoctor' tool

    """

@mcp.tool()
async def doctoravaiable(name:str)->str:
    """provide the information relate to is doctor is free , available,there"""
    doctorname = name.strip().lower()
    doctorname = name.strip().lower().replace(" ", "").replace("dr.", "").replace(".dr","")
    if doctorname == "sitathapa":
        return f"yes, {name} is available in hospital"
    elif doctorname =='amitjoshi':
        return f"yes, {name} is available in hospital"
    elif doctorname =='priyaadhikari':
        return f"yes, {name} is available in hospital"
    elif doctorname =='rameshkarki':
        return f"yes, {name} is available in hospital"
    elif doctorname =='nishashrestha':
        return f"yes, {name} is available in hospital"
    elif doctorname =='rajessharma':
        return f"yes, {name} is available in hospital"
    else:
        return f"No, {name} is not any name or person are worked in hospital"

@mcp.tool()
async def Appointment(person:str,date:date,time:time)->str:
    """provide the information related to booked, booking, appointment,holding"""
    return f"{person} has booked in {date} at {time} "

@mcp.tool()
async def personalNumber(name:str)->str:
    """provide the information of contact number of doctor, phone number of doctor"""
    return f"""
    use the 'contactNumber' tool for to provide the phone number or contact number  of doctor which is available in 
    that tool.
    important point:
    1. if inputed name is not present in the that tool. 
       say like this (contact number of this {name} person is available )
    2. if inputed name is present in the that tool.
       say like this ({name} conatact number is ....)
    """

if __name__ == '__main__':
    mcp.run(transport='stdio')

# groq api or chatgpt ai

