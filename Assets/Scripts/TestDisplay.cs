using UnityEngine;
using System.Collections;

public class TestDisplay : MonoBehaviour {

	public Texture aTexture;
	void OnGUI() {
		if (!aTexture) {
			Debug.LogError("Assign a Texture in the inspector.");
			return;
		}
		GUI.DrawTexture(new Rect(10, 10, Screen.width, Screen.height), aTexture, ScaleMode.ScaleToFit);
	}

	// Use this for initialization
	void Start () {

	}

	// Update is called once per frame
	void Update () {

	}
}
