package lists;

import java.util.Collection;
import java.awt.*;
import java.util.LinkedList;
import java.util.Collection;
import java.util.Iterator;

public class lists {

	public String name;
	public String number;

	// Contact constructor
	lists( String n, String num ) {
	name = n;
	number = num;
	   }
	
	public static void main (String[] args) {
	// old array code commented out or deleted

	// create LinkedList 
	LinkedList contactList = new LinkedList();

	// add 5 Contacts to list 
	contactList.add(new lists( "George Washington","(800) 555-1234" )); 
	contactList.add(new lists( "John Adams", "(800) 555-4567" ));
	contactList.add(new lists( "Thomas Jefferson", "(800) 555-7890" ));
	contactList.add(new lists( "James Madison", "(800) 555-3456" ));
	contactList.add(new lists( "James Monroe", "(800) 555-2345" ));


	// get first and last Contact from list
	//lists first = (lists)contactList.getFirst();
	//lists last = (lists)contactList.getLast();
	search(contactList,"George Washington");
	search(contactList,"James Monroe");
	search(contactList,"Andrew Jackson");

	// print out contact info
	//System.out.println(first.name + ": " + first.number );
	//System.out.println(last.name + ": " + last.number );
	}
	private static void search(Collection contacts, String targetName)
	{
	   for (Iterator myIterator=contacts.iterator(); myIterator.hasNext(); ) 
	   {
	      // get the next element 
	      lists c = (lists) myIterator.next();
	      if (c.name.equalsIgnoreCase(targetName))
	      {
	         // print out name and number
	         System.out.println( c.name + ": " + c.number );   

	         // all done searching, exit loop early
	         return; 
	      }
	   } 
	   System.out.println( targetName + ": NOT FOUND");
	} 
}