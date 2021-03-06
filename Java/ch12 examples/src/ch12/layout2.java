package ch12;
import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;

import java.awt.*;

public class layout2 {
	JFrame myFrame;
	JButton appleButton;
	JButton orangeButton;
	JButton pearButton;
	JButton bananaButton;
	JLabel myLabel;

	public static void main(String[] args) {
		new layout2();

	}

	public layout2() {
		myFrame = new JFrame();
		myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		myFrame.setSize(550, 150);
		myFrame.setLocation(200, 300);
		JPanel myPanel = (JPanel)myFrame.getContentPane();
		myPanel.setLayout(new BoxLayout(myPanel,BoxLayout.Y_AXIS));
		
		JPanel topPanel = new JPanel();
		topPanel.setLayout(new FlowLayout());
		topPanel.setBorder(BorderFactory.createLineBorder(Color.BLACK,2));
		myLabel = new JLabel("What is your favorite fruit?");
		topPanel.add(myLabel);
		
		JPanel bottomPanel = new JPanel();
		bottomPanel.setLayout(new GridLayout(2,2,2,2));
		bottomPanel.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
		
		bottomPanel.add(new JButton("Apple"));
		bottomPanel.add(new JButton("Orange"));
		bottomPanel.add(new JButton("Pear"));
		bottomPanel.add(new JButton("Banana"));
		
		myPanel.add(topPanel);
		myPanel.add(bottomPanel);

		myFrame.setVisible(true); 
		 
	}
	

}
