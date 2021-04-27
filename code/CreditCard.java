public  class CreditCard extends Card{
    
    private String limit;
    private String recentArrear;
    
    public void setLimit(String limit){
        this.limit =  limit;
    };
    public String getLimit(){
        return this.limit;
    };
    public void setRecentarrear(String recentArrear){
        this.recentArrear =  recentArrear;
    };
    public String getRecentarrear(){
        return this.recentArrear;
    };
    
    public void repay(){};    
    
}