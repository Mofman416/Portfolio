// File used to register within the Register system

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.util.List;

import javax.swing.*;

public class logR implements ActionListener{
    JFrame regFrame;
    JPanel mainPanel;
    JTextField name;
    JTextField password;
    JButton reg;
    JButton cancel;


    public logR() {
        regFrame = new JFrame("Register New Employee");
        regFrame.setLayout(new FlowLayout());
        regFrame.setLocationRelativeTo(null);

        JPanel mainPanel = (JPanel)regFrame.getContentPane();
        mainPanel.setLayout(new BoxLayout(mainPanel,BoxLayout.Y_AXIS));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // Text field asking for employee name
        JPanel rfield = new JPanel();
        JLabel rname = new JLabel("Enter Your Full Name:");
        rfield.add(rname);
        name = new JTextField(20);
        rfield.add(name);
        mainPanel.add(rfield);

        // Text field asking for employee username
        JPanel pfield = new JPanel();
        JLabel pname = new JLabel("Input Employee Number:");
        pfield.add(pname);
        password = new JTextField(20);
        pfield.add(password);
        mainPanel.add(pfield);

        // Register and Cancel Buttons
        JPanel buttons = new JPanel();
        reg = new JButton("Register");
        reg.addActionListener(this);
        buttons.add(reg);
        cancel = new JButton("Cancel");
        cancel.addActionListener(this);
        buttons.add(cancel);
        mainPanel.add(buttons);

        // Adjusts GUI size with contents and sets the entire GUI the be visible.
        regFrame.pack();
        regFrame.setVisible(true);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Object control = e.getSource();
        if (control==cancel) {
            regFrame.dispose();
        }
    }
}
