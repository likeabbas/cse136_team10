import java.text.SimpleDateFormat;
import java.util.*;

class HelloWorld {
  public static void main(String[] args) {

    //Initialize Date and colors
    String timeStamp = (new java.util.Date()).toLocaleString();
    String[] colors  = {"aqua", "black", "blue", "fuchsia", "gray", "green", "lime",
        "maroon", "navy", "olive","purple", "red", "silver", "teal", "white", "yellow"};
    String textColor = "black";

    //Grab random number from 0 -15
    Random rand = new Random();
    int randomNum = rand.nextInt(16);

    String backgroundColor  = colors[randomNum];

    if(backgroundColor == "black" || backgroundColor == "navy") textColor = "white";
    String document = String.format("<!doctype html> \n"
      + "<body style = 'background-color: %s'>"
      + "<h1 style = 'color:%s'> Hello World from Java @ %s </h1>"
      + "</body> "
      +"</html>", backgroundColor , textColor ,  timeStamp);
      
    System.out.println("Content-Type: text/html");
    System.out.print(document);
  }
}
