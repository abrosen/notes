import java.nio.*;

import java.net.*;
import java.io.*;

public class XKCDDownloader {
	
	
	public static void main(String args[]) {
		int currentComic =  22;
		

		String imgHeader= "http://imgs.xkcd.com/comics/";
		try {
			URL  url = new URL("http://xkcd.com/"+currentComic);
			BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
			String line;
			while(true){ 
				line = br.readLine();
				if(line == null ){
					break;
				}
				if(line.contains(imgHeader)) {
					int start = line.indexOf(imgHeader);
					URL imgUrl = new URL(line.substring(start));
					
					//InputStream imgStream = imgURL.openStream();
					Path out = new File("./"+currentComic).toPath();
					//Files.copy(imgStream, out);

					
					System.out.println(start);
					System.out.println(line.substring(start));

				}
			}	
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

}
