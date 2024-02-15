import "./style.css";
import Map from "ol/Map.js";
import { View } from "ol";
import GeoJSON from "ol/format/GeoJSON";
import MultiPoint from "ol/geom/MultiPoint.js";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
import { Circle as CircleStyle, Fill, Stroke, Style } from "ol/style.js";
import VectorSource from "ol/source/Vector";
import { Vector as VectorLayer } from "ol/layer";
import { fromLonLat } from "ol/proj";

const styles = [
  new Style({
    stroke: new Stroke({
      color: "blue",
      width: 3,
    }),
    fill: new Fill({
      color: "rgba(0, 0, 255, 0.1)",
    }),
  }),
  new Style({
    geometry: function (feature) {
      const coordinates = feature.getGeometry().getCoordinates()[0];
      return new MultiPoint(coordinates);
    },
  }),
];
const source = new VectorSource({
  url: "./polygon.geojson",
  format: new GeoJSON(),
});

const layer = new VectorLayer({
  source: source,
  style: styles,
});

const map = new Map({
  layers: [
    new TileLayer({
      source: new OSM(),
    }),
  ],
  target: "map",
  view: new View({
    center: fromLonLat([16.889444444444443, 46.294166666666655]),
    zoom: 7.5,
  }),
});
map.addLayer(layer);
