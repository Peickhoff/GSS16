
public class Timer {
	public static void main(String[] args) {
		char[] a = {'a','b','c','d'};
		char[] b = {'a','b','c','d'};
		char[] c = {'a','b','f','e'};
		Timer t = new Timer();
		System.out.println(t.timeAttack(a,b));
		System.out.println(t.timeAttack(a,c));
	}

	long timeAttack(char[] a, char[] b) {
		long startTime = 0;
		long endTime = 0;
		long deltaTime = 0;
		
		startTime = System.nanoTime();
		passwordCompare(a,b);
		endTime = System.nanoTime();
		deltaTime = endTime - startTime;
		return deltaTime;
	}
	
	boolean passwordCompare(char[] a,char[] b) {
		int i;
		if (a.length != b.length) return false;
		for
		(i=0; i<a.length && a[i]==b[i]; i++);
		return i == a.length;
	}
}
