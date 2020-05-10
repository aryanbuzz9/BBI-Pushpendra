
class Singleton 
{ 

	 static Singleton single_object=null; 

	public String str; 

	private Singleton() 
	{ 
		str = "This is a Singleton class"; 
	} 

	public static Singleton Singleton() 
	{ 

		if (single_object == null) 
		{ 
			single_object = new Singleton(); 
		} 
		return single_object; 
	} 
} 

class Main 
{ 
	public static void main(String args[]) 
	{ 
		// instantiating Singleton class with variable x 
		Singleton obj = Singleton.Singleton(); 


		System.out.println(obj.str); 

	} 
} 
