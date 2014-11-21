import java.util.Random;

/* This is the program that tests the page replacement algorithms
 * each method returns the number of page faults
 * @author Andrew Rosen
 */


public class FaultTest {
	public static int[] reference = {1,1,2,3,7,4,3,5,1,2,4,2,1,5,3,6,7,2,3,7,6,4,3,2,1,7,6,3};
	
	public static int lru(){
		// These contain the page frame entries.
		int[] frame = {-1,-1,-1,-1,-1,-1};
		
		// to ease readability, we will make a separate array for the clock
		// the clock keeps track of how many uses have passed between the last use of the page
		int[] clock = { 0, 0, 0, 0, 0, 0};
		
		// finally, this int keeps track of the number of page faults.
		int faults = 0;
		
		for(int i=0; i<reference.length;i++){
			int position = contains(reference[i],frame);
			if(position>-1){
				clock[position]=0;
				printFrames(frame, false);
			}
			else{
				faults++;
				int replace = findLRU(clock);
				//System.out.println("Fault. Replacing "+ frame[replace]+ " with " + reference[i] + ".");
				frame[replace]= reference[i];
				clock[replace]= 0;
				printFrames(frame, true);
			}
			increment(clock);
		}

		
		return faults;
	}
	
	
	public static int optimal(){
		// These contain the page frame entries.
		int[] frame = {-1,-1,-1,-1,-1,-1};
		
		// finally, this int keeps track of the number of page faults.
		int faults = 0;
		
		
		for(int i=0; i<reference.length;i++){
			int position = contains(reference[i],frame);
			if(position>-1){
				printFrames(frame, false);
			}
			else{
				faults++;
				frame[findNext(frame, i)]= reference[i];
				printFrames(frame, true);
			}
		}
		
		return faults;
	}
	
	public static int reserve(){
		// These contain the page frame entries.
		int[] frame = {-1,-1,-1};
		int[] common= {1,2,3};
		
		// finally, this int keeps track of the number of page faults.
		int faults = 3;
		Random random = new Random();
		System.out.println("Reserved: [ 1 2 3 ]");
		for(int i=0; i<reference.length;i++){
			int position = contains(reference[i],frame);
			int inCommon= contains(reference[i],common);
			int temp= contains(-1,frame);
			if(position>-1||inCommon>-1){
				printFrames(frame, false);
			}
			else if(temp>-1){
				faults++;
				frame[temp]= reference[i];
				printFrames(frame, true);
			}
			else{
				faults++;
				frame[random.nextInt(3)]=reference[i];
				printFrames(frame, true);
			}
		}

		
		return faults;
	}
	


	public static void main(String[] args){
		System.out.println("LRU output:");
		int lru= lru();
		System.out.println("\n\n\nLRU faults: "+lru+ "\n\n\nOptimal output:");
		int optimal = optimal();
		System.out.println("\n\n\nOptimal faults: "+optimal+"\n\n\nReserved output:");
		int reserve = reserve();
		System.out.println("\n\n\nReserve faults: "+reserve);
	}
	
	public static int contains(int x, int[] arr){
		for(int i=0; i<arr.length; i++){
			if(arr[i]==x)
			{
				return i;
			}
		}
		return -1;
	}
	
	public static int findLRU(int[] arr){
		int max = -1;
		int ret = 0;
		for(int i=0; i<arr.length;i++){
			if(arr[i]>max){
				max=arr[i];
				ret=i;
			}
		}
		return ret;
	}
	
	
	public static void printFrames(int[] arr, boolean fault){
		System.out.print("[");
		for(int i=0; i<arr.length;i++){
			if(arr[i]==-1)
				System.out.print(" _");
			else
				System.out.print(" " +arr[i]);
		}
		System.out.print(" ]");
		if(fault){ 
			System.out.print("[ x ]\n"); 
		}
		else{
			System.out.print("[   ]\n");
		}
	}


	//test for return
	public static void increment(int[] arr){
		for(int i= 0; i<arr.length; i++){
			arr[i]++;
		}
	}
	
	public static int findNext(int[] arr, int pos){
		int steps = 0;
		int ret = 0;
		for(int i= 0; i<arr.length; i++){
			int temp = findNext(arr[i],pos);
			if(temp>steps){
				steps=temp;
				ret=i;
			}
		}
		return ret;
	}
	
	public static int findNext(int val, int pos){
		int steps = 0;
		for(int i=pos+1; i<reference.length; i++){
			steps++;
			if(reference[i]== val){
				break;
			}
		}
		return steps;
	}
}
