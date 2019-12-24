class ProjectTest {
    public static void main(String[] args) {
        Project project1 = new Project("XXX", "YYY");
        Project project2 = new Project();
        // project1.setName("Maintenance");
        // project1.setDescription("oil change");
        project2.setName("Income");
        project2.setDescription("Drivers income");
        String project1Name = project1.getName();
        String project2Name = project2.getName();
        String project1Description = project1.getDescription();
        String project2Description = project2.getDescription();
        System.out.println("Project1 - Name: " + project1Name + ", Description: " + project1Description);
        System.out.println("Project1 - Name: " + project2Name + ", Description: " + project2Description);
    }
}
