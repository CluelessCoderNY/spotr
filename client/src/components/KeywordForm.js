import React, { useState } from "react";
import { Form, FormField, Input, Button } from "semantic-ui-react";

export const KeywordForm = ({ onNewKeyword }) => {
  const [keyword, setKeyword] = useState("");

  return (
    <Form>
      <FormField>
        <Input
          placeholder={"Enter new keyword"}
          value={keyword}
          onChange={e => setKeyword(e.target.value)}
        />
      </FormField>
      <FormField>
        <Button
          onClick={async () => {
            const key = { keyword };
            const response = await fetch("/createkeyword", {
              method: "POST",
              headers: {
                "Content-Type": "application/json"
              },
              body: JSON.stringify(key)
            });

            if (response.ok) {
              console.log("Response Worked!");
              onNewKeyword(key);
              setKeyword("");
            }
          }}
        >
          Submit
        </Button>
      </FormField>
    </Form>
  );
};
