import javax.swing.JButton;
import javax.swing.JFrame;
import java.awt.*;
import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.JPanel;
import javax.swing.border.*;
import javax.swing.JLabel;

public class PhoneDialer {
	JButton one;
	JButton two;
	JButton three;
	JButton four;
	JButton five;
	JButton six;
	JButton seven;
	JButton eight;
	JButton nine;
	JButton dash;
	JButton zero;
	JButton pound;
	JButton dialnumber;
	JFrame dialer;
	JLabel phonelabel;

	public static void main(String[] args) {
		new PhoneDialer();

	}

	public PhoneDialer() {
		dialer = new JFrame();
		dialer.setSize(200, 250);
		dialer.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JPanel panel = (JPanel)dialer.getContentPane();
		panel.setLayout(new BoxLayout(panel,BoxLayout.Y_AXIS));
		Border myBorder = BorderFactory.createEmptyBorder(10,10,10,10);
		panel.setBorder(myBorder);
		
		JPanel toplabel = new JPanel();
		toplabel.setLayout(new FlowLayout());
		phonelabel = new JLabel("Enter the Number");
		toplabel.add(phonelabel);
		
		one = new JButton("1");
		two = new JButton("2");
		three = new JButton("3");
		four = new JButton("4");
		five = new JButton("5");
		six = new JButton("6");
		seven = new JButton("7");
		eight = new JButton("8");
		nine = new JButton("9");
		dash = new JButton("-");
		zero = new JButton("0");
		pound = new JButton("#");
		dialnumber = new JButton("Dial Number");
		
		JPanel numgrid = new JPanel();
		numgrid.setLayout(new GridLayout(4,3,5,5));
		numgrid.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
		
		numgrid.add(new JButton("1"));
		numgrid.add(new JButton("2"));
		numgrid.add(new JButton("3"));
		numgrid.add(new JButton("4"));
		numgrid.add(new JButton("5"));
		numgrid.add(new JButton("6"));
		numgrid.add(new JButton("7"));
		numgrid.add(new JButton("8"));
		numgrid.add(new JButton("9"));
		numgrid.add(new JButton("-"));
		numgrid.add(new JButton("0"));
		numgrid.add(new JButton("#"));
		
		panel.add(toplabel);
		panel.add(numgrid);
		
		dialer.setVisible(true);
	}

}
