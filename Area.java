// This class calculates the area of 2D shapes

class Area{
	// variables
	private double length;
	private double width;
	private double height;
	private double base;

	// constructor
	public Area(double l, double w, double h, double b){
		length = l;
		width = w;
		height = h;
		base = b;
	}

	// getters
	public double getLength(){
		return length;
	}
	public double getWidth(){
		return width;
	}
	public double getHeight(){
		return height;
	}
	public double getBase(){
		return base;
	}
	// settters
	public void setLength(double l){
		length = l;
	}
	public void setWidth(double w){
		width = w;
	}
	public void setHeight(double h){
		height = h;
	}
	public void setBase(double b){
		base = b;
	}

	// methods
	public double calcRect(){
		return (length * width);
	}
	public double calcTri(){
		return (base * height * (1/2));
	}
	public double calcTrap(){
		return ((length + base)/2) * height;
	}

	// main
	public static void main(String[] args){
		System.out.println("Welcome to Area!");
		Job = Area(2,3,4,5);

		System.out.println("Length: " + Job.getLength());
		System.out.println("Width: " + Job.getWidth());
		System.out.println("Height: " + Job.getHeight());
		System.out.println("Base: " + Job.getBase());
	}
}
