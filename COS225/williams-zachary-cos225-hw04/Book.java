
public class Book {
	public String title;
	public String genre;
	
	public Book(String title, String genre) {
		this.title = title;
		this.genre = genre;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}
	
	public String ToString(Book book) {
		return "" + book.getTitle();
	}
}
