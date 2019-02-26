import java.awt.*;
import javax.swing.*;

public class PizzaPlace {
	JFrame pizzaFrame;
	JPanel mainPanel;
	
	public static void main(String[] args) {
		new PizzaPlace();

	}

	public PizzaPlace() {
		JFrame pizzaFrame = new JFrame();
		pizzaFrame.setLayout(new FlowLayout());
		pizzaFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JPanel mainPanel = (JPanel)pizzaFrame.getContentPane();
		mainPanel.setLayout(new BoxLayout(mainPanel,BoxLayout.Y_AXIS));
		mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
		
		
		
		
		
		
		
		
		
		
		
		pizzaFrame.pack();
		pizzaFrame.setVisible(true);
	}

}
