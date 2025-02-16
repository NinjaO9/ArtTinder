import React, { useState } from "react";
import "./ArtistCard.css";

const ArtistCard: React.FC = () => {
  const [artistName, setArtistName] = useState("Artist Name");
  const [about, setAbout] = useState("This is a brief description about the artist.");
  const [image, setImage] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  const handleImageUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      setImage(URL.createObjectURL(event.target.files[0]));
    }
  };

  const handleAction = (liked: boolean) => {
    setMessage(liked ? "Liked Picture" : "Disliked Image");

    setTimeout(() => {
      window.location.reload();
    }, 2000);
  };

  return (
    <div className="artist-page">
      {message ? (
        <div className={`fullscreen-message ${message === "Liked Picture" ? "liked" : "disliked"}`}>
          <h1>{message}</h1>
        </div>
      ) : (
        <>
          <button className="exit-button">EXIT</button>

          <div className="artist-content">
            <input
              type="text"
              value={artistName}
              onChange={(e) => setArtistName(e.target.value)}
              className="artist-name-input"
              disabled={message !== null}
            />

            <div className="image-upload">
              {image ? (
                <img src={image} alt="Uploaded Artwork" className="artwork" />
              ) : (
                <label className="upload-label">
                  Upload Image
                  <input type="file" accept="image/*" onChange={handleImageUpload} disabled={message !== null} />
                </label>
              )}
            </div>

            <textarea
              className="about-input"
              value={about}
              onChange={(e) => setAbout(e.target.value)}
              disabled={message !== null}
            />

            <div className="buttons">
              <button className="reject" onClick={() => handleAction(false)} disabled={message !== null}>✖</button>
              <button className="accept" onClick={() => handleAction(true)} disabled={message !== null}>✔</button>
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default ArtistCard;
