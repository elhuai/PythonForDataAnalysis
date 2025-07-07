import argparse
import pandas as pd

def create_pivot_table(csv_path):
    """
    從 CSV 檔案讀取資料並建立樞紐分析表。

    Args:
        csv_path (str): 輸入的 CSV 檔案路徑。

    Returns:
        pandas.DataFrame: 產生的樞紐分析表。
    """
    df = pd.read_csv(csv_path)
    pivot_table = df.pivot_table(values='total_bill', index=['size', 'smoker'], columns=['day', 'time'], aggfunc='sum')
    return pivot_table

def export_to_excel(df, excel_path):
    """
    將 DataFrame 匯出至 Excel 檔案。

    Args:
        df (pandas.DataFrame): 要匯出的 DataFrame。
        excel_path (str): 輸出的 Excel 檔案路徑。
    """
    df.to_excel(excel_path, sheet_name='Pivot Table')

def main():
    """
    主函式，用於處理命令列參數和執行核心邏輯。
    """
    parser = argparse.ArgumentParser(description='從 CSV 檔案建立樞紐分析表並匯出至 Excel。')
    parser.add_argument('--csv', required=True, help='輸入的 CSV 檔案路徑。')
    parser.add_argument('--excel', required=True, help='輸出的 Excel 檔案路徑。')
    
    args = parser.parse_args()
    
    try:
        pivot_df = create_pivot_table(args.csv)
        print("成功建立樞紐分析表。")
    except FileNotFoundError:
        print(f"錯誤：找不到指定的 CSV 檔案：{args.csv}")
        return
    except Exception as e:
        print(f"建立樞紐分析表時發生錯誤：{e}")
        return

    try:
        export_to_excel(pivot_df, args.excel)
        print(f"成功將樞紐分析表匯出至 {args.excel}。")
    except Exception as e:
        print(f"匯出 Excel 檔案時發生錯誤：{e}")

if __name__ == '__main__':
    main()