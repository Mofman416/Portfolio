// Michael Freeman

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;

import javax.swing.*;

public class cashRegister implements ActionListener {
    JFrame cashFrame;
    JPanel mainPanel;
    JTextField cname;


    public static void main(String[] args) {
        new cashRegister();

    }

    public cashRegister() {
        // This is the frame for the register
        JFrame cashFrame = new JFrame("Cash Register");
        cashFrame.setLayout(new FlowLayout());
        cashFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


        JPanel mainPanel = (JPanel)cashFrame.getContentPane();
        mainPanel.setLayout(new BoxLayout(mainPanel,BoxLayout.Y_AXIS));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // Text field test
        //Text field asking for the customer name.
        JPanel tfield = new JPanel();
        JLabel name1 = new JLabel("Customer Name:");
        tfield.add(name1);
        cname = new JTextField(20);
        tfield.add(cname);
        mainPanel.add(tfield);

        // Adjusts GUI size with contents and sets the entire GUI the be visible.
        cashFrame.pack();
        cashFrame.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {

    }
}
