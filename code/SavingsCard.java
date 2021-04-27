public  class SavingsCard extends Card{
    
    private String balance;
    private String rate;
    
    public void setBalance(String balance){
        this.balance =  balance;
    };
    public String getBalance(){
        return this.balance;
    };
    public void setRate(String rate){
        this.rate =  rate;
    };
    public String getRate(){
        return this.rate;
    };
    
    public void deposit(){};    
    
}