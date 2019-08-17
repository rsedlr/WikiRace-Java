package com.rsedlr.WikiRace;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Connect {
  /**
   * Connect to a sample database
   */
  public static void connect() {
    Connection conn = null;
    try {
      String url = "jdbc:sqlite:wikiLinksDev.sqlite";
      conn = DriverManager.getConnection(url);
      System.out.println("Connection to SQLite has been established.");

    } catch (SQLException e) {
      System.out.println(e.getMessage());
    } finally {
      try {
        if (conn != null) {
          conn.close();
        }
      } catch (SQLException ex) {
        System.out.println(ex.getMessage());
      }
    }
  }

  /**
   * @param args the command line arguments
   */
  public static void main(String[] args) {
    System.out.println("this bit yh");
    connect();
  }
}