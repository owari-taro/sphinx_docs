================
diary
================


.. toctree::
   :maxdepth: 2
   :caption: Contents:
    
    diary_202404





--------------
2024/3/4
--------------

セキュリティ試験
===============
* djangoを使ったwebappでセキュリティ関連のsettingに漏れがないかのcheckができる
https://qiita.com/juchilian/items/3afa2d679fb88bd70aff

* seurityツールによってはよりセキュリティ的には厳しいsettingしていたときになぜか失敗をあげてくるばあいもがある 
  

-------------
2023/3/5
-------------
* デフォルトだとドメイン名自動更新
* whois レジストリごと


----------------
2024/3/28
----------------
powershell
=========================
powershellではすべてがobjectであり、
例えば文字型の場合、↓みたいにメソッド,プロパティがていぎできる


::

    > $color="red"
    #文字列の長さ
    > $color.Length
    3
    > Get-Member -InputObject $color
    

   TypeName: System.String

    Name             MemberType            Definition
    ----             ----------            ----------
    Clone            Method                System.Object Clone(), System.Object ICloneable.Clone()
    CompareTo        Method                int CompareTo(System.Object value), int CompareTo(string strB), int IComparab...
    Contains         Method                bool Contains(string value)
    CopyTo           Method                void CopyTo(int sourceIndex, char[] destination, int destinationIndex, int co...
    EndsWith         Method                bool EndsWith(string value), bool EndsWith(string value, System.StringCompari...
    Equals           Method                bool Equals(System.Object obj), bool Equals(string value), bool Equals(string...
    GetEnumerator    Method                System.CharEnumerator GetEnumerator(), System.Collections.IEnumerator IEnumer...
    GetHashCode      Method                int GetHashCode()
    GetType          Method                type GetType()
    GetTypeCode      Method                System.TypeCode GetTypeCode(), System.TypeCode IConvertible.GetTypeCode()
    IndexOf          Method                int IndexOf(char value), int IndexOf(char value, int startIndex), int IndexOf...
    IndexOfAny       Method                int IndexOfAny(char[] anyOf), int IndexOfAny(char[] anyOf, int startIndex), i...
    Insert           Method                string Insert(int startIndex, string value)
    IsNormalized     Method                bool IsNormalized(), bool IsNormalized(System.Text.NormalizationForm normaliz...
    LastIndexOf      Method                int LastIndexOf(char value), int LastIndexOf(char value, int startIndex), int...
    LastIndexOfAny   Method                int LastIndexOfAny(char[] anyOf), int LastIndexOfAny(char[] anyOf, int startI...
    Normalize        Method                string Normalize(), string Normalize(System.Text.NormalizationForm normalizat...
    PadLeft          Method                string PadLeft(int totalWidth), string PadLeft(int totalWidth, char paddingChar)
    PadRight         Method                string PadRight(int totalWidth), string PadRight(int totalWidth, char padding...
    Remove           Method                string Remove(int startIndex, int count), string Remove(int startIndex)
    Replace          Method                string Replace(char oldChar, char newChar), string Replace(string oldValue, s...
    Split            Method                string[] Split(Params char[] separator), string[] Split(char[] separator, int...
    StartsWith       Method                bool StartsWith(string value), bool StartsWith(string value, System.StringCom...
    Substring        Method                string Substring(int startIndex), string Substring(int startIndex, int length)
    ToBoolean        Method                bool IConvertible.ToBoolean(System.IFormatProvider provider)
    ToByte           Method                byte IConvertible.ToByte(System.IFormatProvider provider)
    ToChar           Method                char IConvertible.ToChar(System.IFormatProvider provider)
    ToCharArray      Method                char[] ToCharArray(), char[] ToCharArray(int startIndex, int length)
    ToDateTime       Method                datetime IConvertible.ToDateTime(System.IFormatProvider provider)
    ToDecimal        Method                decimal IConvertible.ToDecimal(System.IFormatProvider provider)
    ToDouble         Method                double IConvertible.ToDouble(System.IFormatProvider provider)
    ToInt16          Method                int16 IConvertible.ToInt16(System.IFormatProvider provider)
    ToInt32          Method                int IConvertible.ToInt32(System.IFormatProvider provider)
    ToInt64          Method                long IConvertible.ToInt64(System.IFormatProvider provider)
    ToLower          Method                string ToLower(), string ToLower(cultureinfo culture)
    ToLowerInvariant Method                string ToLowerInvariant()
    ToSByte          Method                sbyte IConvertible.ToSByte(System.IFormatProvider provider)
    ToSingle         Method                float IConvertible.ToSingle(System.IFormatProvider provider)
    ToString         Method                string ToString(), string ToString(System.IFormatProvider provider), string I...
    ToType           Method                System.Object IConvertible.ToType(type conversionType, System.IFormatProvider...
    ToUInt16         Method                uint16 IConvertible.ToUInt16(System.IFormatProvider provider)
    ToUInt32         Method                uint32 IConvertible.ToUInt32(System.IFormatProvider provider)
    ToUInt64         Method                uint64 IConvertible.ToUInt64(System.IFormatProvider provider)
    ToUpper          Method                string ToUpper(), string ToUpper(cultureinfo culture)
    ToUpperInvariant Method                string ToUpperInvariant()
    Trim             Method                string Trim(Params char[] trimChars), string Trim()
    TrimEnd          Method                string TrimEnd(Params char[] trimChars)
    TrimStart        Method                string TrimStart(Params char[] trimChars)
    Chars            ParameterizedProperty char Chars(int index) {get;}
    Length           Property              int Length {get;}
