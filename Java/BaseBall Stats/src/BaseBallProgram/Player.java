package BaseBallProgram;

public class Player {
	public String PlayerName = ""; 
	
	public int[] hits;
	public int GetTotHits() {
		int tot = 0;
		for(int i: hits) {
			tot +=i;
		}
		return tot;
	}
	
	public double GetAvgHits() {
		int tot = 0;
		for(int i: hits) {
			tot +=i;
		}
		
		
		return (double)tot/(double)25;
	}
}
