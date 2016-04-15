import java.util.*;

class GetPost{
  public static void main(String[] args){

    Map<String,String> env = System.getenv();

    if(env.get("REQUEST_METHOD") == null){
      System.out.println("<h1>No Form was submitted</h1>");
    }
    else if(env.get("REQUEST_METHOD") == "GET"){
      String data = env.get("QUERY_STRING");
    }
    else{
      //CASE FOR POST
    }
  }
}
