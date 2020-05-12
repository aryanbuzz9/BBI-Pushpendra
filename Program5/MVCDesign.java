public class MVCDesign {
   public static void main(String[] args) {
      Student model  = retriveStudentFromDatabase();

      View v = new View();

      Controller c = new Controller(model, view);

      c.updateView();
      c.setStudentName("John");

      c.updateView();
   }

   private static Student retriveStudentFromDatabase(){
      Student student = new Student();
      student.setName("Ashish Sir");
      
      return student;
   }
}
