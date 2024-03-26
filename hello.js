require([
    "esri/Map",
    "esri/views/SceneView",
    "dojo/domReady!"
  ], function(Map, SceneView) {
  
    // Create a map
    var map = new Map({
      basemap: "topo"
    });
  
    // Create a SceneView
    var view = new SceneView({
      container: "viewDiv",
      map: map,
      scale: 50000000,
      center: [0, 0]
    });
  
    // Listen for click events on the view
    view.on("click", function(event) {
      // Query elevation at the clicked location
      view.when().then(function() {
        view.map.ground.queryElevation(event.mapPoint).then(function(result) {
          // Print elevation value to console
          console.log("Elevation:", result.geometry.z);
        });
      });
    });
  });
  