import javax.swing.JButton;
import javax.swing.JFrame;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.JPanel;
import javax.swing.border.*;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

public class PhoneDialer implements ActionListener{
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
	String number = "";

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
		one.addActionListener(this);
		two = new JButton("2");
		two.addActionListener(this);
		three = new JButton("3");
		three.addActionListener(this);
		four = new JButton("4");
		four.addActionListener(this);
		five = new JButton("5");
		five.addActionListener(this);
		six = new JButton("6");
		six.addActionListener(this);
		seven = new JButton("7");
		seven.addActionListener(this);
		eight = new JButton("8");
		eight.addActionListener(this);
		nine = new JButton("9");
		nine.addActionListener(this);
		dash = new JButton("-");
		dash.addActionListener(this);
		zero = new JButton("0");
		zero.addActionListener(this);
		pound = new JButton("#");
		pound.addActionListener(this);
		
		
		JPanel numgrid = new JPanel();
		numgrid.setLayout(new GridLayout(4,3,5,5));
		numgrid.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
		
		numgrid.add(one);
		numgrid.add(two);
		numgrid.add(three);
		numgrid.add(four);
		numgrid.add(five);
		numgrid.add(six);
		numgrid.add(seven);
		numgrid.add(eight);
		numgrid.add(nine);
		numgrid.add(dash);
		numgrid.add(zero);
		numgrid.add(pound);
		
		panel.add(toplabel);
		panel.add(numgrid);
		dialnumber = new JButton("Dial Number");
		dialnumber.addActionListener(this);
		dialnumber.setAlignmentX(Component.CENTER_ALIGNMENT);
		panel.add(dialnumber);
		
		
		dialer.setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent event) {
		Object control = event.getSource();
		System.out.print(control);
		
		if (control == dialnumber) {
			JOptionPane.showMessageDialog(dialer, "Dialing:"+number);
			number = "";
		}
		else if (control == one) {
			number = number + "1";
			System.out.print(number);
		}
		else if (control == two) {
			number = number + "2";
		}
		else if (control == three) {
			number += "3";
		}
		else if (control == four) {
			number += "4";
		}
		else if (control == five) {
			number += "5";
		}
		else if (control == six) {
			number += "6";
		}
		else if (control == seven) {
			number += "7";
		}
		else if (control == eight) {
			number += "8";
		}
		else if (control == nine) {
			number += "9";
		}
		else if (control == dash) {
			number += "-";
		}
		else if (control == zero) {
			number += "0";
		}
		else if (control == pound) {
			number += "#";
		}
		
		
	}

}
