from typing import List

def merge_sort(data) -> None:
void merge(int arr[],int LeftInd,int RightInd,int MiddleInd)
{
  int i,j,k;
  int n1=MiddleInd-LeftInd+1;
  int n2=RightInd-MiddleInd;
  int L[n1],R[n2];
  for(i=0;i<n;i++)
  {
    L[i]=arr[LeftInd+i];
  }
  for(j=0;j<n;j++)
  {
    R[j]=arr[MiddleInd+1+j];
  }
  i=0,j=0,k=LeftInd;
  while(i<n1 && j<n2)
  {
    if(L[i]<=R[j])
    {
      arr[k]=L[i];
      i++;
    }
    else
    {
      arr[k]=R[j];
      j++;
    }
    k++;
  while(i<n1)
  {
    arr[k]=L[i];
    i++;
    k++;
  }
  while(j<n2)
  {
    arr[k]=R[j];
    j++;
    k++;
  }
  }
}
      
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
