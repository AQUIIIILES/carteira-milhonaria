import Tooltip from "@mui/material/Tooltip";
import Chip from "@mui/material/Chip";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";

function GridHeader({ title }) {
  return (
    <Tooltip title={title.replace(/<br\s*\/?>/g, " ")}>
      <span
        className="custom-header-title"
        style={{
          whiteSpace: "pre-line",
          textAlign: "center",
          display: "block",
          width: "100%",
        }}
        dangerouslySetInnerHTML={{
          __html: title.replace(/\n/g, "<br />"),
        }}
      />
    </Tooltip>
  );
}

function GridTitle({ title }) {
  return (
    <Tooltip title={title}>
      <span>{title}</span>
    </Tooltip>
  );
}

function GridRow({ formattedValue }) {
  return (
    <Tooltip title={formattedValue}>
      <span>{formattedValue}</span>
    </Tooltip>
  );
}

function GridRowLucro({ formattedValue, value }) {
  return (
    <Tooltip title={formattedValue}>
            {value > 0 ? (
              <Chip
                label={formattedValue}
                color="success"
                icon={<TrendingUpIcon />}
              />
            ) : value < 0 ? (
              <Chip
                label={formattedValue}
                color="error"
                icon={<TrendingDownIcon />}
              />
            ) : (
              <Chip label={formattedValue} />
            )}
          </Tooltip>
  );
}

export { GridHeader, GridTitle, GridRow, GridRowLucro }