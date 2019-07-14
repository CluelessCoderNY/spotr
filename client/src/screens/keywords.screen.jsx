import React, { useEffect, useState } from "react";
import { Keywords } from "../components/Keywords";
import { KeywordForm } from "../components/KeywordForm";
import { Container } from "semantic-ui-react";

export const KeywordScreen = () => {
  const [listing, setListing] = useState([]);

  useEffect(() => {
    fetch("/findkeywords").then(response =>
      response.json().then(data => {
        setListing(data.result);
      })
    );
  }, []);

  console.log(listing);

  return (
    <div className='App'>
      <Container style={{ marginTop: 40 }}>
        <KeywordForm
          onNewKeyword={key =>
            setListing(currentKeywords => [...currentKeywords, key])
          }
        />
        <Keywords listing={listing} />
      </Container>
    </div>
  );
};
