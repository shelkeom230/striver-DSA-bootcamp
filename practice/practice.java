package practice;

public class practice {
   
    public static String revString(String str){
        int n=str.length();
        int left=0,right=n-1;
        char charArray[]=str.toCharArray();
        while(left<right){
            char temp=charArray[left];
            charArray[left]=charArray[right];
            charArray[right]=temp;
            left+=1;
            right-=1;
        }
        return new String(charArray);
    }
    public static float findPerc(int marks){
        float perc=(marks*100) /500.0f;
        return perc; 
    }
    public static void main(String[] args) {
        System.out.println(revString("omkar"));
    }
}