import java.util.*;
import java.io.*;

class GetPost{
  public static void main(String[] args){

    Map<String, String> formData = new HashMap <String, String>();
    Map<String, String> env = System.getenv();
    //String data = "username=danielkong&password=helloworld&magicnumber=5";
    String data = "";
    if(env.get("REQUEST_METHOD") == "GET"){
       data = env.get("QUERY_STRING");
    }
    else if(env.get("REQUEST_METHOD") == "POST") {
      Console console = System.console();
      String line;
      while((line = console.readLine()) != null){
        data = data + line;
      }
    }
    else{
      System.out.println("<h1>There was no GET or POST request submitted through a form!</h1>");
      return;
    }

    String[] formField = data.split("&");

    for(int i = 0; i < formField.length; i++){
      String[] fields = formField[i].split("=");
      formData.put(fields[0],fields[1]);
    }

    try{
      int magicNum = Integer.parseInt(formData.get("magicnumber"));
    }catch(NumberFormatException e){
      System.out.println("<h1> Error parsing magic number </h1>");
      return;
    }

    for(int i = 0; i < magicNum; i++){
      System.out.println("<h1> Hello " + formData.get("username") + " with a password of " + formData.get("password") + " </h1>");
    }

  }
}
