import Chip from "@mui/material/Chip";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import TrendingFlatIcon from "@mui/icons-material/TrendingFlat";
import { formatCurrency } from "../utils/formatters";

function TableValorInvestido({valueTotalInvestido}) {
    return (
        <Chip
            label={ formatCurrency("USD", valueTotalInvestido) }
            color="primary"
            icon={<TrendingFlatIcon />}
        />
    );
}

function TableValorAtual({valueTotalAtual, valueInvestido, valueAtual}) {
    return (
        valueAtual > valueInvestido ? (
            <Chip
                label={ formatCurrency("USD", valueTotalAtual) }
                color="success"
                icon={<TrendingUpIcon />}
            />
            ) : valueAtual < valueInvestido ? (
            <Chip
                label={ formatCurrency("USD", valueTotalAtual) }
                color="error"
                icon={<TrendingDownIcon />}
            />
            ) : (
            <Chip
                label= { formatCurrency("USD", valueTotalAtual) }
            />
        )
    );
}

function TableResult({formattedValue, value}) {
    return (
        value > 0 ? (
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
            <Chip
                label={formattedValue}
            />
        )
    );
}
       
export { TableResult, TableValorInvestido, TableValorAtual };