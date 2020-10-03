class Volume
{
  int vol(int len,int br,int h)
  {
    return(len*br*h); 
  }
  int vol(int r,int h)
  {
    return(((22*r*r)/7)*h); 
  }
  int vol(int r)
  {
     return((4*22*r*r*r)/(3*7));
  }
}
class S2
{
  public static void main(String args[])
  {
     Volume vol1= new Volume();
     System.out.println(" Volume of Cuboid "+vol1.vol(Integer.parseInt(args[0]),Integer.parseInt(args[1]),Integer.parseInt(args[2])));
     System.out.println(" Volume of Cylinder "+vol1.vol(Integer.parseInt(args[3]),Integer.parseInt(args[4])));
     System.out.println(" Volume of Sphere "+vol1.vol(Integer.parseInt(args[5])));
  }
}