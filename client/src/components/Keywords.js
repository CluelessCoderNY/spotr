import React from "react";
import { List, Header } from "semantic-ui-react";

export const Keywords = ({ listing }) => {
  return (
    <List>
      {listing.map(result => {
        return (
          <List.Item key={result.keyword}>
            <Header>{result.keyword}</Header>
          </List.Item>
        );
      })}
    </List>
  );
};
