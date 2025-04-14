"""

This is a MCP server, that interacts with an F5 device using iControl REST API.


"""

from mcp.server.fastmcp import FastMCP
from Tools.F5object import F5_object

# Initialize FastMCP server
mcp = FastMCP("my_f5_mcp_server")


@mcp.tool()
def show_stats_tool(object_name: str, object_type: str):
    """ This tool shows the stats of an object from an F5 device using the iControl REST API.
     Args:
            object_name is the name of the object. 
            object_type can be : virtual,pool,irule or profile  
    """
    stats = F5_object(object_name = object_name, object_type = object_type)
    return stats.stats()

@mcp.tool()
def show_logs_tool(lines_number: str):
    """This tool shows the lines_number of logs from an F5 device using the iControl REST API.
     Args:
            lines_number is the number of lines to be returned.  
    """
    logs = F5_object(lines_number = lines_number)
    return logs.logs()

@mcp.tool()
def list_tool(object_name: str, object_type: str):
    """ This tool lists object on an F5 device using the iControl REST API.
     Args:
            object_name is the name of the object. 
            object_type can be : virtual,pool,irule or profile  
    """
    list = F5_object(object_name = object_name, object_type = object_type)
    return list.list()


@mcp.tool()
def create_tool(url_body: dict, object_type: str):
    """ This tool creates an object on an F5 device using the iControl REST API.
        Args:
            url_body contains the configuration of the pool. 
            object_type can be : virtual,pool,irule or profile  
        The configuration of the object is the body for an POST request.        
       
        """  
    # using python requests
    create = F5_object(url_body = url_body, object_type = object_type)
    return create.create()


@mcp.tool()
def update_tool(url_body: dict, object_type: str, object_name: str):
    """ This tool updates an object on an F5 device using the iControl REST API.
        Args:
            url_body contains the configuration of the pool. 
            object_type can be : virtual,pool,irule or profile
            object_name is the name of the object.

        The configuration of the object is the body for an PATCH request.
       
    """    
    # using python requests
    update = F5_object(url_body = url_body, object_type = object_type,object_name = object_name)
    return update.update()

@mcp.tool()
def delete_tool(object_type: str, object_name: str):
    """ This tool updates an object on an F5 device using the  iControl REST API.
        Args:            
            object_type can be : virtual,pool,irule or profile
            object_name is the name of the object.

        The configuration of the pool is the body for an DELETE request.
       
    """    
    # using python requests
    delete = F5_object(object_type = object_type, object_name = object_name)
    return delete.delete()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
