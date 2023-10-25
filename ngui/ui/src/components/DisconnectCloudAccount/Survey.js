import React from "react";
import { Box, Typography } from "@mui/material";
import { useFormContext } from "react-hook-form";
import { FormattedMessage } from "react-intl";
import { SPACING_2 } from "utils/layouts";
import {
  REASON_VALUE_OTHER,
  FIELD_REASON,
  ReasonsRadioGroup,
  AnswerInput,
  FIELD_CAPABILITIES,
  FIELD_OTHER
} from "./FormElements";

const Survey = () => {
  const { watch } = useFormContext();
  const reason = watch(FIELD_REASON);

  return (
    <>
      <Typography marginBottom={SPACING_2}>
        <FormattedMessage id="disconnectingLastDataSource" />
      </Typography>
      <Box marginBottom={SPACING_2}>
        <ReasonsRadioGroup />
        {reason === REASON_VALUE_OTHER && <AnswerInput labelMessageId={"reason"} name={FIELD_OTHER} />}
      </Box>
      <AnswerInput labelMessageId={"capabilitiesQuestion"} name={FIELD_CAPABILITIES} />
    </>
  );
};

export default Survey;