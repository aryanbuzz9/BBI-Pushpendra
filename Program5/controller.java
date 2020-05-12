public class StudentController {
   private Student model;
   private View v;

   public StudentController(Student model, StudentView view){
      this.model = model;
      this.view = view;
   }

   public void setname(String name){
      model.setName(name);		
   }

   public String getname(){
      return model.getName();		
   }


   public void updateView(){				
      view.printStudentDetails(model.getName());
   }	
}
