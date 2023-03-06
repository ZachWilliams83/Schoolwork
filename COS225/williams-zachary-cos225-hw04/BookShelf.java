import java.util.ArrayList;

public class BookShelf {
	public char firstChar;
	public char letter;
	public String printString;
	public String concatString;
	ArrayList<Book> bookShelf;
	
	public BookShelf() {
		this.bookShelf = new ArrayList<Book>(8);
	}
	
	public BookShelf(char letter){
		this.bookShelf = new ArrayList<Book>(8);
		this.letter = letter;
	}

	public char getLetter(ArrayList<Book> bookShelf) {
		return letter;
	}

	public void setLetter(char letter) {
		this.letter = letter;
	}

	public char getFirstChar(Book book) {
		String bookTitle = book.getTitle();
		firstChar = bookTitle.charAt(0);
		return firstChar;
	}

	public void setFirstChar(char firstChar) {
		this.firstChar = firstChar;
	}

	public ArrayList<Book> getBookShelf() {
		return bookShelf;
	}

	public void setBookShelf(ArrayList<Book> bookShelf) {
		this.bookShelf = bookShelf;
	}
	
	public void addBook(Book book) {
		if (book.getTitle().charAt(0) == getLetter(bookShelf)) {
			bookShelf.add(book);
		}
		else {
			return;
		}
	}
	public void removeBook(Book book) {
		bookShelf.remove(book);
	}
	
	public String ToString() {
		concatString = "";
		if (bookShelf.size() != 0) {
			for (int i = 0; i < bookShelf.size(); i++) {
				printString = bookShelf.get(i).getTitle();
				concatString += printString + "    ";
			}
			return concatString;
		}
		
		return "";
	}
}
