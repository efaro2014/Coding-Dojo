public class BankAccountTest{
    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        account.deposit("checking", 100);
        account.deposit("savings", 1000);
        account.withdraw("checking", 25);
        System.out.println(BankAccount.displayTotal());
        // x = account.BankAccount();
    }
}
