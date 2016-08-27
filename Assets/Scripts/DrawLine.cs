using UnityEngine;
using System.Collections;

//using System.Drawing;
//using Cairo;

public class DrawLine : MonoBehaviour
{
//	private string filename;
//	void drawtest ()
//	{
//		// The using statement ensures that potentially heavy objects
//		// are disposed immediately.
//		using (ImageSurface draw = new ImageSurface (Format.Argb32, 70, 150)){
//			using (Context gr = new Context(draw)){
//				gr.Antialias = Antialias.Subpixel;    // sets the anti-aliasing method
//				gr.LineWidth = 9;          // sets the line width
//				gr.Color = new Cairo.Color (0, 0, 0, 1);   // red, green, blue, alpha
//				gr.MoveTo (10, 10);          // sets the Context's start point.
//				gr.LineTo (40, 60);          // draws a "virtual" line from 5,5 to 20,30
//				gr.Stroke ();          //stroke the line to the image surface
//
//				gr.Antialias = Antialias.Gray;
//				gr.LineWidth = 8;
//				gr.Color = new Cairo.Color (1, 0, 0, 1);
//				gr.LineCap = LineCap.Round;
//				gr.MoveTo (10, 50);
//				gr.LineTo (40, 100);
//				gr.Stroke ();
//
//				gr.Antialias = Antialias.None;    //fastest method but low quality
//				gr.LineWidth = 7;
//				gr.MoveTo (10, 90);
//				gr.LineTo (40, 140);
//				gr.Stroke ();
//
//				draw.WriteToPng (filename);  //save the image as a png image.
//			}
//		}
//	}
//
////	private void createPlant() {
////		Bitmap img = new Bitmap(300, 300);
////		System.Drawing.Graphics g = System.Drawing.Graphics.FromImage(img);
////		Pen line = new Pen (System.Drawing.Color.Black, 4f);
////		g.DrawLine (line, new PointF (5, 100), new PointF (275, 150));
////
////		img.Save(filename);
////
////
////	}
//
//	void Awake() {
//		filename = Application.dataPath + "/testdraw.png";
//	}
//


	//reference to LineRenderer component
	private LineRenderer line; 
	//car to store mouse position on the screen
	private Vector3 mousePos;
	//assign a material to the Line Renderer in the Inspector
	public Material material;
	//number of lines drawn
	private int currLines = 0;

	void Update ()
	{
		//Create new Line on left mouse click(down)
		if(Input.GetMouseButtonDown(0))
		{
//			drawtest ();
//			Debug.Log ("Created file at " + filename);
			//check if there is no line renderer created
			if(line == null){
				//create the line
				createLine();
			}
			//get the mouse position
			mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
			//set the z co ordinate to 0 as we are only interested in the xy axes
			mousePos.z = 0;
			//set the start point and end point of the line renderer
			line.SetPosition(0,mousePos);
			line.SetPosition(1,mousePos);
		}
		//if line renderer exists and left mouse button is click exited (up)
		else if(Input.GetMouseButtonUp(0) && line)
		{
			mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
			mousePos.z = 0;
			//set the end point of the line renderer to current mouse position
			line.SetPosition(1,mousePos);
			//set line as null once the line is created
			line = null;
			currLines++;
		}
		//if mouse button is held clicked and line exists
		else if(Input.GetMouseButton(0) && line)
		{
			mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
			mousePos.z = 0;
			//set the end position as current position but dont set line as null as the mouse click is not exited
			line.SetPosition(1, mousePos);
		}
	}

	//method to create line
	private void createLine()
	{
		//create a new empty gameobject and line renderer component
		line = new GameObject("Line"+currLines).AddComponent<LineRenderer>();
		//assign the material to the line
		line.material =  material;
		//set the number of points to the line
		line.SetVertexCount(2);
		//set the width
		line.SetWidth(0.4f,0.15f);
		//render line to the world origin and not to the object's position
		line.useWorldSpace = true;  
		Debug.Log(Application.dataPath);
	}
}