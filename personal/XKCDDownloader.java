
import java.net.*;
import java.io.*;
public class XKCDDownloader {
	
	
	public static void main(String args[]) {
		int currentComic =  22;
		
		try {
			URL  url = new URL("http://xkcd.com/"+currentComic);
			BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
			String line;
			while(true){ 
				line = br.readLine();
				if(line == null ){
					break;
				}
				System.out.print(line);
			}
			
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}

}
