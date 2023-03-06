import java.util.ArrayList;

public class LibraryTester {
	
	public static void main(String[] args) {
		char letter1 = 'O';
		char letter2 = 'T';
		ArrayList<Book> bookShelf1 = new ArrayList<Book>(8);
		BookShelf shelf1 = new BookShelf(letter1);
		shelf1.setBookShelf(bookShelf1);
		ArrayList<Book> bookShelf2 = new ArrayList<Book>(8);
		BookShelf shelf2 = new BookShelf(letter2);
		shelf2.setBookShelf(bookShelf2);
		System.out.println(shelf1.ToString());
		System.out.println(shelf2.ToString());
		Book book1 = new Book("The Heart of the Betrayed", "Fantasy");
		Book book2 = new Book("Our Hill of Stars", "Crime");
		Book book3 = new Book("One of a Kind", "Romance");
		Book book4 = new Book("The Vision of Roses", "Science Fiction");
		System.out.println(book1.ToString(book1));
		System.out.println(book2.ToString(book2));
		System.out.println(book3.ToString(book3));
		System.out.println(book4.ToString(book4));
		shelf1.addBook(book1);
		shelf1.addBook(book2);
		shelf1.addBook(book3);
		shelf1.addBook(book4);
		shelf2.addBook(book1);
		shelf2.addBook(book2);
		shelf2.addBook(book3);
		shelf2.addBook(book4);
		System.out.println(shelf1.ToString());
		System.out.println(shelf2.ToString());
	}
}
