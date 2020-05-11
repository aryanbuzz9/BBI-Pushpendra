
class Bbi_Training extends Thread{  
public void run(){  
System.out.println("Simple Thread is running...");  
}  
public static void main(String args[]){  
Bbi_Training obj=new Bbi_Training();  
obj.start();  
 }  
}
