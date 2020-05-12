public class Controller {
   private Student model;
   private View v;

   public Controller(Student model, View v){
      this.model = model;
      this.v= v;
   }

   public void setname(String name){
      model.setName(name);		
   }

   public String getname(){
      return model.getName();		
   }


   public void updateView(){				
      view.studentDetails(model.getName());
   }	
}
