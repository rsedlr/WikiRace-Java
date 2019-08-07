import java.sql.*;  

public class Database {

  Connection conn = null;  

  public static void main(String[] args) {  // would be connect() function
    try {  
      String url = "jdbc:sqlite:C:/sqlite/JTP.db";  
      conn = DriverManager.getConnection(url);  
      System.out.println("Connection to SQLite has been established.");  
    } catch (SQLException e) {  
        System.out.println(e.getMessage());  
    }  
  }  


  public static void closeConn(String[] args) {
    conn.close();  
  }


  public static int getLinksCount(String linkDirection, int[] pageIDs) {  // direction should be incoming or outgoing

    if (linkDirection != "incoming" && linkDirection != "outgoing") {
      System.out.println("ERROR: incorrect link direction for getLinksCount()");
      return null
    }

    String query = String.format("SELECT SUM(%s_links_count) FROM links WHERE id IN %s'", sumType, pageIDs);
    
    try {  
      Statement stmt = conn.createStatement();  
      ResultSet rs = stmt.executeQuery(query);  
    } catch (SQLException e) {  
      System.out.println(e.getMessage());  
    }  

    ArrayList <int> result = new ArrayList<String>();
    int columnCount = rs.getMetaData().getColumnCount();
    rs.next();
    for (int i = 1; i <= columnCount ; i++) {
      result.add( rs.getString(i) );
    }
    return result
  } 


  public static int[] getLinks(String linkDirection, int[] pageIDs) {  // direction should be incoming or outgoing
    
    if (linkDirection != "incoming" && linkDirection != "outgoing") {
      System.out.println("ERROR: incorrect link direction for getLinks()");
      return null
    }

    String query = String.format("SELECT id, %s_links FROM links WHERE id IN %s;", sumType, pageIDs);

    try {  
      Statement stmt = conn.createStatement();  
      ResultSet rs = stmt.executeQuery(query);  
    } catch (SQLException e) {  
      System.out.println(e.getMessage());  
    }  

    ArrayList <String> result = new ArrayList<String>();
    int columnCount = rs.getMetaData().getColumnCount();
    rs.next();
    for (int i = 1; i <= columnCount ; i++) {
      result.add( rs.getString(i) );
    }
    return result
  }


  public static String getPageName(int pageID) {

    String query = String.format("SELECT title FROM pages WHERE id = %s;", pageID);

    try {  
      Statement stmt = conn.createStatement();  
      ResultSet rs = stmt.executeQuery(query);  
    } catch (SQLException e) {  
      System.out.println(e.getMessage());  
    }  

    return rs.getString()
  }
} 




