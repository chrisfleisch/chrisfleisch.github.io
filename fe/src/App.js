import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import MyGallery from "./components/Photos";
import SiteFooter from "./components/Footer";
import data from "./data/photos.json";

function App() {
  return (
    <>
      <header className="site-header">
        <div className="container">
          <a className="site-title" href="/">
            Chris Fleisch
          </a>
        </div>
      </header>
      <div className="container page-content">
        <MyGallery photos={data} />
      </div>
      <SiteFooter />
    </>
  );
}

export default App;
