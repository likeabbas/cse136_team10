import java.util.*;

class EnvMap{
	public static void main(String[] args) {

		Map<String, String> env = System.getenv();
		ArrayList <String> browser = new ArrayList <String>();
		ArrayList <String>  server  = new ArrayList <String>();
		for(String envName : env.keySet()){

			if(envName.startsWith("HTTP")){
				browser.add(envName);
			}
			else{
				server.add(envName);
			}
		}
		System.out.print("Content-Type: text/html\n");
		System.out.println("<h2>Browser Variables </h2>");
		System.out.println("<table>");
		System.out.println("<tr><td class = 'header'>Variable Name</td><td class ='header'>Value</td></tr>");

		for(String browserName : browser){
			String row = String.format("<tr><td> %s </td><td> %s </td></tr>",browserName, env.get(browserName));
			System.out.println(row);
		}
		System.out.println("</table>");

		System.out.println("<h2>Browser Variables </h2>");
		System.out.println("<table>");
		System.out.println("<tr><td class = 'header'>Variable Name</td><td class ='header'>Value</td></tr>");

		for(String serverName : server){
			String serverRow = String.format("<tr><td> %s </td><td> %s </td></tr>",serverName, env.get(serverName));
			System.out.println(serverRow);
		}
		System.out.println("</table>");
}
}
