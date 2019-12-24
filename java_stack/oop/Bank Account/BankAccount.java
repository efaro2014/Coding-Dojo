import java.util.Random;
//  Create a BankAccount class.
public class BankAccount{
    // The class should have the following attributes: (string) account number, 
    // (double) checking balance, (double) savings balance.
    private String accountNumber;
    private double checkingBalance;
    private double savingsBalance;
    //  Create a class member (static) that has the number
    //  of accounts created thus far.
    public static int numberOfAccounts;
    // Create a class member (static) that tracks the 
    // total amount of money stored in every account created.
    public static double totalMoney;
    // In the constructor, call the private method i.e each user has a random ten digit account.
    public BankAccount(){
        generateNewAccountNumber();
        numberOfAccounts +=1;
    }
    // Create a getter method for the user's checking account balance.
    public double getCheckingBalance(){
        return this.checkingBalance;
    }
    // getter method for the user's saving account balance.
    public double getSavingBalance(){
        return this.savingsBalance;
    }
    //private method that returns a random ten digit account number
    private String generateNewAccountNumber(){
        String numbers = "0123456789";
        String newAccountNumber = "";

        Random rand = new Random();

        for (int i = 0; i < 5; i++){
            int num = numbers.charAt(rand.nextInt(10));
            newAccountNumber += num; 
        }
        accountNumber = newAccountNumber; 

        return newAccountNumber;
    }
    //  method that will allow a user to deposit money into either 
    // the checking or saving, be sure to add to total amount stored.
    public void deposit(String accountType, double money){
        if (accountType == "saving"){
            this.savingsBalance += money;
        }
        else if(accountType == "checking"){
            this.checkingBalance += money;
        }
        else{
            System.out.println("please choose 'saving or 'checking' ");
        }
        
        totalMoney += money;
    }
    // Create a method to withdraw money from one balance. 
    // Do not allow them to withdraw money if there are insufficient funds.
     public void withdraw(String accountType, double money){
        if (accountType == "checking"){
            if (this.checkingBalance - money <0){
                System.out.println("You have insufficient balance in ur account");
            }
            this.checkingBalance -= money;
        }
        else{
            System.out.println("You can't take money from other account");
        }
        totalMoney -= money;
        System.out.println("You have withdrawn" +money+ "from your checking ac");
    }
    public static double displayTotal(){
        return totalMoney;
    }
}

