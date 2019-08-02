package examples;

import javax.swing.*;

public class exmaple1 {

	public static void main(String[] args) {
		
		String Result = JOptionPane.showInputDialog(null, "What's your favorite color?","Color Picker",JOptionPane.INFORMATION_MESSAGE);
		
		JOptionPane.showMessageDialog(null, "Your favorite color is " + Result, "Color Picker", JOptionPane.INFORMATION_MESSAGE);
	}

}
